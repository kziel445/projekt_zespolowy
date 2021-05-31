<template>
    <form class="columns" v-on:submit.prevent="registerData">
      <div class="column"></div>
      
      <div class="column is-one-quarter block section">
        <div class="title-div">
          <p class="title is-3">Rejestracja</p>
        </div>
        
        <div class="field">
          <div class="label is-small">Nazwa uzytkownika</div>
          <div class="control has-icons-left">
            <input class="input" type="text" placeholder="Nazwa uzytkownika" v-model="register.username" >
            <span class="icon is-small is-left is-link">
            <i class="fa fa-user"></i>
          </span>
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Haslo</div>
          <div class="control has-icons-left">
            <input class="input" type="password" placeholder="Haslo" v-model="register.password" >
            <span class="icon is-small is-left is-link">
            <i class="fa fa-key"></i>
          </span>
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Potwierdz haslo</div>
          <div class="control has-icons-left">
            <input class="input" type="password" placeholder="Potwierdz haslo" v-model="confirmPassword" >
            <span class="icon is-small is-left is-link">
            <i class="fa fa-lock"></i>
          </span>
          </div>
        </div>
        <div class="field ">
          <div class="label is-small">Email</div>
          <div class="control has-icons-left">
            <input class="input" type="text" placeholder="Email" v-model="register.email" >
            <span class="icon is-small is-left is-link">
            <i class="fa fa-envelope-square"></i>
          </span>
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Imie *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Imie" v-model="register.first_name" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Nazwisko *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Nazwisko" v-model="register.last_name" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Miasto *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Miasto" v-model="register.city" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Ulica *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Ulica" v-model="register.street" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Kod-pocztowy *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Kod-pocztowy" v-model="register.zip_code" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Numer domu *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Numer domu" v-model="register.house_number" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Numer mieszkania *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Numer mieszkania" v-model="register.flat_number" >
          </div>
        </div>
        <div class="field">
          <div class="label is-small">Numer telefonu *</div>
          <div class="control">
            <input class="input" type="text" placeholder="Numer telefonu" v-model="register.phone_number" >
          </div>
        </div>
        
        <div class="field is-grouped pt-5">
          <div class="control">
            <button type="submit" class='button is-dark'>Wyslij</button>
          </div>
        </div>
      </div>
      <div class="column"></div>
      
      

    </form>
</template>

<script>
  import { getAPI } from '../axios-api'
  export default {
    name: 'register',
    data () {
      return {
        confirmPassword: "",
        register: {
          username: "",
          email: "",
          password: "",
          first_name: "",
          last_name: "",
          city: "",
          street: "",
          zip_code: "",
          house_number: "",
          flat_number: "",
          phone_number: null,
          
        },
        
      }
    },
    methods: {
      registerData() {
        getAPI.post('/register', this.register)
        .then(response => {
          console.log(response)
        })
        .catch(err => {
          console.log(err)
        })
        this.$router.push({name: 'login'})
      }
    }
    
  }
  
</script>

<style>
.title-div {
  display: flex;
  justify-content: center;
  margin-bottom: 2em;
}
</style>