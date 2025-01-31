vim.g.mapleader = " "

vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.api.nvim_set_keymap('v', '<leader>r', '<Plug>SnipRun', { silent = true })
vim.api.nvim_set_keymap('n', '<leader>r', '<Plug>SnipRun', { silent = true })
vim.api.nvim_set_keymap('n', '<leader>f', '<Plug>SnipRunOperator', { silent = true })

vim.keymap.set('n', 'j', 'gj')
vim.keymap.set('n', 'k', 'gk')
