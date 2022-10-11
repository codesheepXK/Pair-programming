let columnArr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
let column0 = [0, 3, 6]
let column1 = [1, 4, 7]
let column2 = [2, 5, 8]
import { MessageBox } from 'mint-ui';
import Vue from 'vue';
const state = {
    number: 0,
    preNumber: 0,
    isTurn: true,
    isReady: false,
    isRet: false,
    ownBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    otherBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    preOwnBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    preOtherBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
}
const getters = {
    number: state => state.number,
    isTurn: state => state.isTurn,
    isReady: state => state.isReady,
    ownBoard: state => state.ownBoard,
    otherBoard: state => state.otherBoard,
}
const mutations = {
    getNum() {
        state.number = Math.floor(Math.random() * 6) + 1
    },
    retData(state) {
        if (state.isRet) {
            MessageBox.alert("不可以连续撤回")
            return
        }
        state.number = state.preNumber
        for (let i = 0; i < 9; i++) {
            Vue.set(state.ownBoard, i, state.preOwnBoard[i])
        }
        for (let i = 0; i < 9; i++) {
            Vue.set(state.otherBoard, i, state.preOtherBoard[i])
        }
        state.isTurn = !state.isTurn
        state.isRet = true
    },
    updateData(state, { pos, index, data }) {
        console.log(state.ownBoard, state.otherBoard, state.preOwnBoard, state.preOtherBoard);
        state.preNumber = state.number
        state.preOwnBoard = JSON.parse(JSON.stringify(state.ownBoard))
        state.preOtherBoard = JSON.parse(JSON.stringify(state.otherBoard))
        let arr = []
        let column = columnArr[index];
        if (pos == "top") {
            Vue.set(state.otherBoard, index, state.number);
            arr = state.ownBoard;
        } else {
            Vue.set(state.ownBoard, index, state.number);
            arr = state.otherBoard;
        }
        console.log(state.ownBoard, state.otherBoard);
        if (column == 0) {
            column0.forEach(item => {
                if (arr[item] == data)
                    Vue.set(arr, item, 0)
            })
        } else if (column == 1) {
            column1.forEach(item => {
                if (arr[item] == data)
                    Vue.set(arr, item, 0)
            })
        } else if (column == 2) {
            column2.forEach(item => {
                if (arr[item] == data)
                    Vue.set(arr, item, 0)
            })
        }
        if (pos == "top") {
            state.ownBoard = arr;
        } else {
            state.otherBoard = arr;
        }
        state.isRet = false
    },
    updateTurn() {
        state.isTurn = !state.isTurn
    },
    updateReady() {
        state.isReady = !state.isReady
    },
    calSum() {
        let sumOther = 0;
        let sunOwn = 0;
        for (let i = 0; i <= 2; i++) {
            let num = [0, 0, 0, 0, 0, 0, 0]
            if (i == 0) {
                column0.forEach(item => {
                    num[state.otherBoard[item]] += 1;
                })
            }
            if (i == 1) {
                column1.forEach(item => {
                    num[state.otherBoard[item]] += 1;
                })
            }
            if (i == 2) {
                column2.forEach(item => {
                    num[state.otherBoard[item]] += 1;
                })
            }
            for (let j = 1; j <= 6; j++) {
                sumOther += j * num[j] * num[j]
            }
        }
        for (let i = 0; i <= 2; i++) {
            let num = [0, 0, 0, 0, 0, 0, 0]
            if (i == 0) {
                column0.forEach(item => {
                    num[state.ownBoard[item]] += 1;
                })
            }
            if (i == 1) {
                column1.forEach(item => {
                    num[state.ownBoard[item]] += 1;
                })
            }
            if (i == 2) {
                column2.forEach(item => {
                    num[state.ownBoard[item]] += 1;
                })
            }
            for (let j = 1; j <= 6; j++) {
                sunOwn += j * num[j] * num[j]
            }
        }
        MessageBox.alert(sumOther + ":" + sunOwn, "游戏结束")
    },
}
const actions = {
    checkOver({ commit }, { pos }) {
        let flag = true;
        if (pos == "top") {
            for (let i = 0; i < state.otherBoard.length; i++) {
                if (state.otherBoard[i] == 0) {
                    flag = false;
                    break;
                }
            }
        } else {
            for (let i = 0; i < state.ownBoard.length; i++) {
                if (state.ownBoard[i] == 0) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) {
            commit('calSum')
        }
    }

}


export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}
