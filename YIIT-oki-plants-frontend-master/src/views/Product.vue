<template>
    <div class="page-product">
        <div class="column my-flex box">
            <figure class="image box">
                <img v-bind:src="product.get_image">
            </figure>
            
            <div class="prize-container">
                <h2 class="subtitle">{{ product.name }} - Oki-Plants</h2>
                <p><strong>Cena: </strong>{{ product.cost }}zł</p>
                <p><strong>Dostępna ilość: </strong>{{ product.amount }} sztuk</p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input class="input" type="number" min="1" v-model="amount">
                    </div>

                    <div class="control">
                        <div class="button is-success" @click="addToCart">Dodaj do koszyka</div>
                    </div>
                </div>  
            </div>
        
        </div>
        <div class="column">
            <div class="info box">
                <h1 class="title">Opis</h1>
                <p>{{ product.description }}</p>
            </div>
            
        </div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            amount: 1
        }
    },
    mounted() {
        this.getProduct()
        
    },
    
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await getAPI.get(`products/${category_slug}/${product_slug}`)
            .then(response => {
                this.product = response.data
                document.title = `${this.product.name} | Oki-plants`
            })
            .catch(err => {
                console.log(error)
            })

            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if(isNaN(this.amount) || this.amount < 1) {
                this.amount = 1
            }
            
            const item = {
                product: this.product,
                amount: this.amount
            }
            this.$store.commit('addToCart', item)

            toast({
                message: "Produkt został dodany do koszyka",
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right'
            })
        }
    }

}
</script>

<style lang="scss" scoped>
    
    .image {
        display:flex;
        justify-content: center;
        margin-right: 2em;
    }
    .page-product {
        border-top: 1px solid rgb(247, 247, 247);
    }
    .my-flex {
        display:flex;
        justify-content: center;
        margin-top: 3em;
    }

    
    .info {
        display: flex;
        justify-content: center;
        flex-flow: column wrap;
        margin: 5% 14% 0 14%;
        
    }
</style>