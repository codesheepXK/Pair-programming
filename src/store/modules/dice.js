let columnArr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
let column0 = [0, 3, 6]
let column1 = [1, 4, 7]
let column2 = [2, 5, 8]
import { MessageBox } from 'mint-ui';
import Vue from 'vue';
const state = {
    number: 0,
    isTurn: true,
    isReady: false,
    ownBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    otherBoard: [0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    updateData(state, { pos, index, data }) {
        let arr = []
        let column = columnArr[index];
        if (pos == "top") {
            arr = state.ownBoard;
        } else {
            arr = state.otherBoard;
        }
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
        state.otherBoard.forEach(item => {
            sumOther += item;
        });
        state.ownBoard.forEach(item => {
            sunOwn += item;
        })
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