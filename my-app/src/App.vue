<template>
  <v-app>
    <v-main>
      <main-screen/>
    </v-main>
  </v-app>
</template>

<script>
import MainScreen from './components/MainScreen';


export default {
  name: 'App',

  components: {
    MainScreen
   
  },

  data: () => ({
   
  }
  ),
};
</script>
