# 安裝package
`poetry install`

# 執行虛擬環境
`poetry shell`

# 執行unit test
* `python -m unittest -v`
* `python -m unittest -v test.test_logic_version.TestLogicVersion.test_version_always_correct`

# unittest
* 名稱建議都以`test`開頭，在unittest自動discover時才會被找到

# Naming Convention
* function: snake_case
* variable: snake_case
* class: CamelCase
* module(filename): snake_case
* package(folder): alllowercase