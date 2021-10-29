<template>
    <v-col cols="12">
        <my-table :orders="items" @passOrderEvent="orderEvent"></my-table>
      </v-col>
</template>


<script>
import MyTable from './SimpleTable.vue'
export default {
     components:{
      MyTable,
    },

    methods:{
        orderEvent(orderStatus){
            console.log("trigger from table component!")
            console.log(orderStatus)
        }
    },

    data(){
        return{
            items:[
                {
                    orderName:"#c91018",
                    company:"happy PLT",
                    customerName: "Jhone Lenno",
                    orderDate: "77",
                    deliveredAmount:33.5,
                    totalAmount:22.9,
                }
            ],
        }
    }
    
}
</script>