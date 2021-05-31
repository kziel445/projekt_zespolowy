<template>
    <div class="column is-4">
        <div class="box">
            <figure class="image mb-4 box">
                <img v-bind:src="product.get_thumbnail">
            </figure>
            <h3>{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ product.cost }}zł</p>

            <router-link v-bind:to="product.get_absolute_url" class="button is-link mt-4">Wyświetl produkt</router-link>
        </div>
    </div>

</template>

<script>

export default {
    name: 'ProductBox',
    props: {
        product: Object,
    }
}

</script>