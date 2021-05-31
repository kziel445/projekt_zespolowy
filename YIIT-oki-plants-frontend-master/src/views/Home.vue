<template>
  <div class="home">
    <section class="hero is-large mb-6 img-background is-success">
      <div class="hero-body has-text-centered ">
        <p class="title mb-6">
          Witaj w internetowym sklepie ogrodniczym Oki-Plants
        </p>
        <p class="subtitle">
          Zbiór wielu gatunków roślin w zasięgu twojej ręki
        </p>
      </div>
    </section>

    <div class="columns is-multiline custom-margin">
      <div class="column is-12">
        <h2 class="is-size2 has-text-centered"><i>Najczęściej Wybierane Produkty</i></h2>
      </div>
      <ProductBox
        v-for="product in commonProducts" 
        v-bind:key="product.id"
        v-bind:product="product"/>
      
    </div>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

import ProductBox from '../components/ProductBox'
export default {
  name: 'home',
  data() {
    return {
      commonProducts: []
    }
  },
  components: {
    ProductBox,
  },
  mounted() {
      this.getCommonProducts()

      document.title = 'Strona Domowa | Oki-plants'
  },
  methods: {
    async getCommonProducts() {
      this.$store.commit('setIsLoading', true)
      getAPI.get('/common-products')
      .then(response => {
        this.commonProducts = response.data
      })
      .catch(err => {
        console.log(err)
      })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style lang="scss" scoped>
  
  .img-background {
    background-image: url("../assets/Header.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    
  }
  
  

  .footer p {
    padding-top: 10em;
  }

  .box {
    background: rgb(247, 247, 247);
  }
  
  .column h2 {
    text-decoration: underline;
  }

  .custom-margin{
    margin: 0 7em 0 7em;
  
}
  
</style>
  
  

