<template>
    <v-simple-table>
        <template>
             <thead>
                <tr>
                <th class="text-left">
                    Order name
                </th>
                <th class="">
                    Customer company
                </th>
                <th class="">
                    Customer name
                </th>
                <th class="">
                    <div>
                        Order date&nbsp;  
                    <v-icon
                    small
                    left
                    @click="passOrderEvent"
                    >
                        fa fa-sort
                    </v-icon>
                        
                    </div>
                   
      
                </th>
                <th class="">
                   Delivered amount
                </th>
                <th class="text-left">
                    Toal amount
                </th>
                </tr>
            </thead>
      <tbody>
        <tr
          v-for="item in orders"
          :key="item.orderName"
        >
          <td>{{ item.orderName }}</td>
          <td>{{ item.company }}</td>
          <td>{{ item.customerName }}</td>
          <td>{{ computeValue(item.orderDate) }}</td>
          <td>{{ item.deliveredAmount }}</td>
          <td>{{ item.totalAmount }}</td>
        </tr>
      </tbody>
        </template>
    </v-simple-table>
</template>

<script>
export default {
    props:["orders"],
    methods:{
        click(){
            console.log("kk")
        },
        computeValue(value){
            return value+1;
        },
        passOrderEvent(){
            if(this.orderStatus === 'NotOdered'){
                this.orderStatus = 'Aesc'
            }
            else if(this.orderStatus === 'Aesc'){
                this.orderStatus = 'Desc'
            }else{
                this.orderStatus = 'Aesc'
            }
            this.$emit('passOrderEvent', this.orderStatus)
        }
    },
    data(){
        return{
            orderStatus:"NotOdered",  // NotOrdered, Aesc, Desc
            
        }
    }
}
</script>

<style lang="css" scoped>
td {
  text-align: left;
}
</style>