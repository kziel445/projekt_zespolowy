<template>
    <tr>
       <td>
           <img v-bind:src="item.product.get_thumbnail">
       </td>
        <td>
            <router-link :to="item.product.get_absolute_url">
               {{ item.product.name }} 
            </router-link>
        </td>
        <td>{{ item.product.cost }} zł</td>
        <td>
            
            
            <div class="is-flex">
                <input class="custom-input" type="number" :value="item.amount" disabled>
                <div>
                    <a @click="decrementAmount(item) "><i class="fa fa-minus-circle" aria-hidden="true"></i></a>
                    <a @click="incrementAmount(item)"><i class="fa fa-plus-circle" aria-hidden="true"></i></a>
                </div>
                
            </div>
            
            
                
            
            
        </td>
        <td>{{ getItemTotal(item).toFixed(2) }} zł</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
import { toast } from 'bulma-toast'
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem,
            
        }
    },
    
    methods: {
        getItemTotal(item) {
            
            return item.amount * item.product.cost
        },
        decrementAmount(item) {
            item.amount--
            if (item.amount === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        incrementAmount(item) {
            if(item.amount < item.product.amount) {item.amount++}
            else {
                toast({
                message: "Ilość przekracza zasoby magazynu",
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'center'
                })
            }
            
            this.updateCart()
        },
        updateCart() {
            
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
    },
}
</script>

<style>
.custom-input {
    width: 2.3em;
    margin-right: .5em;
    background-color: white;
}

input[type=number]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    
}
img {
    width: 50px;
    height: 50px;

}

</style>