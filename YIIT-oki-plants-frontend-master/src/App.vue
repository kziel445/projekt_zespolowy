<template>
  <div id="wrapper">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Oki-Plants</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Czego szukasz" name="query">
                </div>

                <div class="control">
                  <button class="button is-primary">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/" class="navbar-item">Strona Domowa</router-link>
          <router-link :key="$route.path" to="/products" class="navbar-item">Sklep</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-primary">Zaloguj</router-link>
              

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Koszyk ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-center" v-bind:class="{'is-loading': $store.state.isLoading} ">
      <div class="lsd-dual-ring"></div>
    </div>

   
    <router-view/>
    <footer class="footer">
      <div class="content has-text-centered">
      <p>
        <strong>Oki-Plants website</strong> stworzona przez <a href="#">YIIT - Your Innovative</a>. 
      </p>
      </div>
    </footer>
  </div>
  
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    
    cartTotalLength() {
      let total = 0

      for(let i =0; i < this.cart.items.length; i++) {
        total += parseInt(this.cart.items[i].amount)
      }

      return total
    }
  },
}
</script>


<style lang="scss">
  @import '../node_modules/bulma';

  .navbar {
    box-shadow:  0px 2px 4px #ebebeb;
  }
  .footer{
    height: 1em;
    margin-top: 10em;
  }

  .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }

  .lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 94px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }

  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .is-loading-ba {
    height: 0;
    overflow: hidden;

    -webkit-transition: all 0.3s;

    &.is-loading {
      height: 80px;
    }
  }
  
</style>
