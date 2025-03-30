vim.opt.nu = true
-- vim.opt.relativenumber = true

vim.opt.tabstop = 2

vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2

vim.opt.expandtab = true

vim.opt.smartindent = true

vim.opt.wrap = false

vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.undofile = true

vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.termguicolors = true

vim.opt.scrolloff = 8
vim.opt.signcolumn = "yes"
vim.opt.isfname:append("@-@")

vim.opt.updatetime = 50

vim.o.wrap = true
vim.o.linebreak = true -- breaks by word rather than character

vim.api.nvim_set_option("clipboard", "unnamedplus")

if (vim.loop.os_uname().sysname == "Windows_NT")
then
  vim.opt.undodir = os.getenv("homepath") .. "/.vim/undodir"

  vim.o.shell = "pwsh.exe"
  vim.opt.shellcmdflag = '-nologo -noprofile -ExecutionPolicy RemoteSigned -command'
  vim.opt.shellxquote = ''
else
  vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
end
