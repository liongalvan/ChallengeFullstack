import React, {useState, useEffect} from 'react';
import { getProviders } from './services/providers';
import Bank from './bank';

function ElectionBanks(){
const [bank, setBank] = useState()

useEffect(
  ()=>{
    getProviders()
    .then(data=>{
      console.log("data", data)
      if(data.results){
        setBank(data.results)
      }
    })
    .catch(e=>{
      console.log(e)
    })
  }
)


  return(
    <div>
      {bank.map(bank=>< Bank datos={bank} />)}
    </div>
  )
}

export default ElectionBanks;