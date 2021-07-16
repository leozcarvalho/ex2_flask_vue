import Vue from 'vue';
import Router from 'vue-router';
import Numbers from '../components/Numbers.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Numbers',
      component: Numbers,
    },
  ],
});
