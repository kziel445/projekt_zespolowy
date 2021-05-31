<template>
    <div class="page-search">
        <div class="column is-multiline">
            <div class="column is-12">
                
                <h2 class="is-size-5 has-text-grey">Wynik wyszukiwania dla frazy: "{{ query }}"</h2>
            </div>
            <ProductBox 
                v-for="product in products" 
                v-bind:key="product.id"
                v-bind:product="product"/>
        </div>

    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import ProductBox from '../components/ProductBox'
export default {
    name: "Search",
    components: {
        ProductBox
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Wyszukiwarka | Oki-plants'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if(params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await getAPI.post('products/search/', {'query': this.query})
            .then(response => {
                this.products = response.data
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>