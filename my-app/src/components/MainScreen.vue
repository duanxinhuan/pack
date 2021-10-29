<template>
  <v-container>
    <v-row class="text-center">
      <table-component></table-component>

    </v-row>
  </v-container>
</template>

<script>
  import tableComponent from './table/Tablecomponent.vue'
  
  export default {
    components:{
      tableComponent
    },
   
    name: 'HelloWorld',

    data: () => ({
     
    }),
  }
</script>
