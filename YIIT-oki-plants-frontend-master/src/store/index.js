import { createStore } from 'vuex'
import { getAPI } from '../axios-api'

export default createStore({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: '',
    cart: {
      items: [],
    },
    isLoading: false,
    
  },
  mutations: {
    

    updateStorage (state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
      
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
    },
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if(exists.length) {
        exists[0].amount = parseInt(exists[0].amount) + parseInt(item.amount)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    }
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    }

  },
  actions: {
    userLogout(context) {
      if(context.getters.loggedIn) {
        context.commit('destroyToken')

        localStorage.clear();
      }
    },
    
    userLogin (context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI.post('/api-token', {
          username: usercredentials.username,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh }) 
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },


  },
  
})
