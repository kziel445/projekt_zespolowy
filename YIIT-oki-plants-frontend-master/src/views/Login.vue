<template>
    <form class="columns" v-on:submit.prevent="login">
        <div class="column is-one-third"></div>
        <div class="column is-one-third section">
            <div class="title-div">
                <p class="title is-3">Login</p>
            </div>
            <div class="field margin">
                <div class="label is-small">Nazwa uzytkownika</div>
                <div class="control">
                <input class="input" type="text" placeholder="Nazwa uzytkownika" v-model="username" >
            </div>
            <div class="field margin">
                <div class="label is-small">Haslo</div>
                <div class="control">
                <input class="input" type="password" placeholder="Haslo" v-model="password" >
            </div>
            <div class="control margin">
                <button type="submit" class='button is-primary'>Zaloguj</button>
            </div>
            <p class="help">Jeśli nie masz konta - <router-link to="/register"  >Zarejestruj się</router-link ></p>

        </div>
        </div>  
            <div class="column is-one-third"></div>
            
        </div>
        
        
    </form>
</template>

<script>
    export default {
        name: 'login',
        data () {
            return {
                username: '',
                password: '',
                incorrectAuth: false
            }
        },
        methods: {
            login() {
                this.$store.dispatch('userLogin', {
                    username: this.username,
                    password: this.password
                })
                .then(() => {
                    this.$router.push({ name: 'home' })
                })
                .catch(err => {
                    console.log(err)
                    this.incorrectAuth = true
                })
            }
        }
    }
</script>

<style>
.margin {
    margin-top: 7px;
}
</style>

