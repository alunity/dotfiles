import os
import shutil
from pathlib import Path
import git
from typing import List
from datetime import datetime

from git.repo import Repo


def setup_directory(target_dir: str) -> None:
    """
    Create target directory if it doesn't exist

    Args:
        target_dir (str): Path to the target directory
    """
    Path(target_dir).rmdir()


def copy_items(items: List[str], source_dir: str, target_dir: str) -> None:
    """
    Copy files and directories from source to target directory

    Args:
        items (List[str]): List of files or directories to copy
        source_dir (str): Source directory path
        target_dir (str): Target directory path
    """
    for item in items:
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        if not os.path.exists(source_path):
            print(f"Warning: {item} not found in source directory")
            continue

        try:
            if os.path.isfile(source_path):
                # Copy file with metadata
                shutil.copy2(source_path, target_path)
                print(f"Copied file: {item}")
            elif os.path.isdir(source_path):
                # Copy directory and its contents
                if os.path.exists(target_path):
                    shutil.rmtree(target_path)  # Remove existing directory
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                print(f"Copied directory: {item}")
        except Exception as e:
            print(f"Error copying {item}: {str(e)}")


def clone(repo_path: str):
    # Check if repo exists
    if not os.path.exists(os.path.join(repo_path, ".git")):
        # Clone if it doesn't exist
        git.Repo.clone_from("git@github.com:alunity/dotfiles.git", repo_path)
        repo = git.Repo(repo_path)
    else:
        # Open existing repo
        repo = git.Repo(repo_path)
    return repo


def git_operations(repo: Repo) -> None:
    """
    Handle Git operations: add, commit, and push

    Args:
        repo_path (str): Path to the Git repository
    """
    try:
        # Add all changes
        repo.git.add(".")

        # Get current UTC time for commit message
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Commit changes with timestamp
        repo.index.commit(current_time)

        # Push changes to remote
        origin = repo.remote(name="origin")
        origin.push()

        print(
            f"Successfully pushed changes to remote repository with timestamp: {current_time}"
        )
    except git.GitCommandError as e:
        print(f"Git operation failed: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    # Configuration
    source_directory = "/home/alunity"  # Replace with your source directory
    target_directory = "/tmp/dotfiles"  # Replace with your target directory

    home_files: list[str] = [
        ".config/hypr",
        ".config/kitty",
        ".config/nvim",
        ".config/paru",
        ".config/systemd",
        ".config/waybar",
        ".config/code-flags.conf",
        ".config/spotify-flags.conf",
        ".config/uxplayrc",
        "scripts",
        ".bashrc",
        ".haskeline",
    ]

    # Store current working directory
    original_dir = os.getcwd()

    try:
        # setup_directory(target_directory)
        r = clone(target_directory)

        # Copy files
        copy_items(home_files, source_directory, target_directory)

        # Change to target directory for git operations
        os.chdir(target_directory)

        # Perform git operations
        git_operations(r)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Always return to original directory
        os.chdir(original_dir)


if __name__ == "__main__":
    main()
