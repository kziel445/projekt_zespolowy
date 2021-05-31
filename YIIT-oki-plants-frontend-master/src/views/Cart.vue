<template>
    <div class="page-cart">
        <div class="column is-multiline">
            <div class="column is-12">
                <div class="title is-3 mt-4 margin-title">Koszyk</div>
                
            </div>

            <div class="column box mt-5 margin">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th></th>
                            <th>Produkt</th>
                            <th>Cena</th>
                            <th>Ilość</th>
                            <th>Razem</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item" 
                            v-on:removeFromCart="removeFromCart" />
                            
                    </tbody>
                </table>

                <p v-else>Nie masz żadnych produktów w koszyku</p>

                
            </div>
           
        </div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import CartItem from '../components/CartItem'
export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.amount
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.amount
            }, 0)
        },
    }
}
</script>

<style>
.margin {
    margin: 0 9em 0 9em;
}

.margin-title {
    margin-left: 5em;
}
</style>