<template>
     <div class="page-category">
         <div class="column is-12 defualt-margin">
                <h1 class='is-size-2 has-text-centered'>Oki-plants</h1>
            </div>
         <div class="filter-bar">
             <div class="select-container">
                 <span>Filtry: </span>
                 <div class="select">
                     <select v-model="selected">
                        <option selected disabled></option>
                        <option value="all">Wszystkie</option>
                        <option 
                        v-for="cat in categories"
                        v-bind:key="cat.name"
                        v-bind:cat="cat"
                        :value="cat.get_absolute_url"
                        >{{ cat.name  }}</option>
                         
                     </select>
                     
                 </div>
                 <span class="order" >Sortowanie: </span>
                 <div class="select">
                     <select v-model="order">
                        <option selected disabled></option>
                        <option value="name-asc">Alfabetycznie, A-Z</option>
                        <option value="name-desc">Alfabetycznie, Z-A</option>
                        <option value="price-asc">Cena, Rosnąco</option>
                        <option value="price-desc">Cena, Malejąco</option>
                        
                         
                     </select>
                     
                 </div>
             </div>
             
         </div>
         <div class="products-wrapper">
         <div v-if="selected  === '' || selected  === 'all'" class="columns is-multiline">
             
            
             <ProductBox 
                v-for="product in products" 
                v-bind:key="product.id"
                v-bind:product="product"/>
        </div>
        
        <div v-else class="columns is-multiline">
            <div class="column is-12">
                <h2 class='is-size-4 has-text-centered custom-margin'>{{ category.name }}</h2>
            </div>
            
            <ProductBox
                v-for="product in category.products" 
                v-bind:key="product.id"
                v-bind:product="product"/>
        </div>
       </div>

    </div>
</template>

<script>

import { getAPI } from '../axios-api'
import { toast } from 'bulma-toast'

import ProductBox from '../components/ProductBox'
import Category from '../components/Category'

export default {
    name: 'Shop',
    components: {
        ProductBox,
        Category
    },
    data() {
        return {
            products: {},
            category: {
                products: []
            },
            categories: {},
            selected: '',
            order: '',
            
        }
        
    },
    
    mounted() {
        this.getCategory()
        this.getAllProducts()
        this.getCategoryName()
        this.sortProducts()
        
    },
    watch: {
        selected: {
            handler: 'getCategory'
        },

        order: {
            handler: 'sortProducts'
        }
        
        
    },
    methods: {

        sortProducts() {
            
            if(this.order === 'name-asc') {
                
                this.products.sort((a, b) => {
                let fa = a.name.toLowerCase(),
                fb = b.name.toLowerCase();

                if (fa < fb) {
                    return -1;
                }
                if (fa > fb) {
                    return 1;
                }
                    return 0;
                });

                this.category.products.sort((a, b) => {
                let fa = a.name.toLowerCase()
                let fb = b.name.toLowerCase()

                if (fa < fb) {
                    return -1;
                }
                if (fa > fb) {
                    return 1;
                }
                    return 0;
                });
                
            } else if(this.order === 'name-desc') {

                this.products.sort((a, b) => {
                let fa = a.name.toLowerCase(),
                fb = b.name.toLowerCase();

                if (fa > fb) {
                    return -1;
                }
                if (fa < fb) {
                    return 1;
                }
                    return 0;
                });

                this.category.products.sort((a, b) => {
                let fa = a.name.toLowerCase()
                let fb = b.name.toLowerCase()

                if (fa > fb) {
                    return -1;
                }
                if (fa < fb) {
                    return 1;
                }
                    return 0;
                });
            } else if(this.order === 'price-asc') {

                this.products.sort((a, b) => a.cost - b.cost)
                this.category.products.sort((a, b) => a.cost - b.cost)

            } else if(this.order === 'price-desc'){
                this.products.sort((a, b) => b.cost - a.cost)
                this.category.products.sort((a, b) => b.cost - a.cost)
            }
        },

        changeRoute() {
            
            if(this.selected !== 'all') {
                this.$router.push({path: `/products${this.selected}`})
                
            }else {
                
                this.$router.push({path: `/products`})
                
            }

            
        },
        

        async  getAllProducts() {
            this.$store.commit('setIsLoading', true)
            
            await getAPI.get('products')
            .then(response => {
                this.products = response.data
                
                document.title = "Sklep | Oki-plants"
            })
            .catch(err => {
                console.log(err)
            })
        },
        async getCategory() {
            const categorySlug = this.selected
            this.$store.commit('setIsLoading', true)
            this.order = ''
            
            if (this.selected === 'all' || this.selected === "") {return}

            await getAPI.get(`products${categorySlug}`)
            .then(response => {
                this.category = response.data
               
                document.title = `${this.category.name} | Oki-plants`
            })
            .catch(err => {
                console.log(err)

                toast({
                    message: 'Coś poszło nie tak. Proszę spróbuj ponownie',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })
            })


        },
        async getCategoryName() {
            await getAPI.get('categories/')
            .then(response => {
                this.categories = response.data
                
            })
            .catch(err => {
                console.log(err)
            })
        }
        
    }
}
</script>

<style >
.defualt-margin {
    
    display:flex;
    height: 10em;
    justify-content: center;
    align-items: center;
    
}

.select-container {
    display: flex;
    border-top: 1px solid #ebebeb;
    padding: 1.5em;
    
    
    
}

.select-container span {
    justify-self: center;
    align-self: center;
    margin-right: 1em;
    
}


.columns {
    margin-top: 1em;
}

.order {
    margin-left: 1em;
}

.filter-bar {
    margin: 0 7em 0 7em;
}

.products-wrapper {
    margin: 0 7em 0 7em;
  
}

.custom-margin {
    margin-bottom: 1em;
}

</style>