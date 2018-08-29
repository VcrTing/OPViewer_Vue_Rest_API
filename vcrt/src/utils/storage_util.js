/*
    使用 localStroage 存储数据的工具模块

    函数: 一个功能
    对象: 多个功能

*/
const DATA_KEY = 'data_key'

export default {
    save_data (data, data_key) {
        window.localStorage.setItem(data_key||DATA_KEY, JSON.stringify(data))
    },
    
    read_data (data_key) {
        return JSON.parse(window.localStorage.getItem(data_key||DATA_KEY) || null)
    },

    remove_data (data_key) {
        window.localStorage.removeItem(data_key||DATA_KEY)
    }
}