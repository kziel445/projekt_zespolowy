import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home'
import Login from '../views/Login'
import Logout from '../components/Logout'
import Register from '../views/Register'
import Product from '../views/Product'
import About from '../views/About'
import Shop from '../views/Shop'
import Search from '../views/Search'
import Cart from '../views/Cart'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
        requiresLogin: true
      }
    },
    {
    path: '/login',
    name: 'login',
    component: Login,
    },
    {
    path: '/logout',
    name: 'logout',
    component: Logout,
    },
    {
    path: '/register',
    name: 'register',
    component: Register,
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart,
      
    },
    {
      path: '/products/:category_slug?',
      name: 'shop',
      component: Shop,
      alias: '/products/:category_slug'
    },
    {
      path: '/:category_slug/:product_slug',
      name: 'product',
      component: Product,
    },
    
    
    
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
