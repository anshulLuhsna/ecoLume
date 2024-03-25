"use client"

import React, { useState, useEffect } from 'react';
import { Select, Label, TextInput } from 'flowbite-react';
import { Button } from 'flowbite-react';
import ReactDataGrid from  "@inovua/reactdatagrid-community";
import "@inovua/reactdatagrid-community/index.css";
import Papa from 'papaparse';
import {DataGrid} from '@mui/x-data-grid';
import uuidv4 from "uuid"
import { Card } from 'flowbite-react';

function Solar() {
    const [gridData , setGridData] = useState([])
    const [state, setState] = useState("")
    const [budget, setBudget] = useState("")
    const [data, setData] = useState([]);
    const [installationType, setInstallationType] = useState(0); // New state for installation type
    const [panelType, setPanelType] = useState(0); // New state for panel type
    const [capacity, setCapacity] = useState(0); // New state for capacity
    const [maintenanceFrequency, setMaintenanceFrequency] = useState(0); // New state for maintenance frequency
    const [region, setRegion] = useState(0); // New state for region
    const [typeOfInstallation, setTypeOfInstallation] = useState(0); // New state for type of installation
    const [warranty, setWarranty] = useState(0); // New state for warranty
    const [installerName, setInstallerName] = useState(0)
    const [predictBudget, setPredictBudget] = useState(1000000)
    const [predictedAnnualSavings, setPredictedAnnualSavings] = useState(null)
    const [breakEvenPoint, setBreakEvenPoint] = useState(null)
    const handlePredictBudget = (e)=>{
      setPredictBudget(parseInt(e.target.value))
    }
    const handleInstallationType = (e)=>{
      setInstallationType(parseInt(e.target.value))
    }
    const handleInstallerName = (e)=>{
      setInstallerName(parseInt(e.target.value))
    }
    const handlePanelType = (e)=>{
      setPanelType(parseInt(e.target.value))
    }
    const handleCapacity = (e)=>{
      setCapacity(parseInt(e.target.value))
    }
    const handleMaintainance = (e)=>{
      setMaintenanceFrequency(parseInt(e.target.value))
    }
    const handleRegion = (e)=>{
      setRegion(parseInt(e.target.value))
    }
    const handleTypeOfInstallation = (e)=>{
      setTypeOfInstallation(parseInt(e.target.value))
    }
    const handleWarranty = (e)=>{
      setWarranty(parseInt(e.target.value))
    }


    const columns = [
      {field: 'id', headerName: 'ID', width: 100, align:"center"},
      {
        field: 'EnergyProduced',
        headerName: 'Energy produced (kWh)',
        width: 200,
        align: 'center'
      },
      {
        field: 'InstallerName',
        headerName: 'Installer Brand',
        width: 200,
        align: 'center'
      },
      {
        field: 'TypeOfInstallation',
        headerName: 'Type of panel',
        width: 200,
        align: 'center'
      },
      
      {
        field: 'AnnualSavings',
        headerName: 'Annual savings (Rs)',
        width: 150,
        align: 'center'
      }
    ];
    useEffect(() => {

      // Construct the URL to the JSON file
  
      const url = 'csvjson.json'; // Adjust the path based on your file's location within the public folder
  
  
  
      // Fetch the JSON data
  
      fetch(url)
  
        .then((response) => response.json())
  
        .then((jsonData) => {
  
          // Use the JSON data
          console.log(jsonData)
          setData(jsonData);
  
        })
  
        .catch((error) => {
  
          console.error('Error fetching JSON:', error);
  
        });
  
    }, []); // Empty dependency array means this effect runs once on mount
  
  
  
    if (!data) {
  
      return <div>Loading...</div>;
  
    }
    const rows = [
      {
        "id": "1",
        "userId": "2",
        "title": "3",
        "completed": "4"
      }
    ]
    const handleStateChange = (e) => {
      console.log(parseInt(e.target.value))
        setState(parseInt(e.target.value))
    }
    const handleBudgetChange = (e) => {
        setBudget(parseInt(e.target.value))
    }

    const handleSortGrid = () => {
      // Filter data based on selected state
      console.log(state)
      console.log(data)
    //   let sortedDataRegion = data.filter(row => {
    //     console.log(row.Region);
    //     return row.Region == parseInt(region);
    // });
      let sortedDataRegion = data.filter(row => row.Region === state)
      // Filter data based on selected budget
      let sortedDataBudget = sortedDataRegion.filter(row => row.Cost <= parseInt(budget));
  
      // Sort filtered data based on budget
      sortedDataBudget.sort((a, b) => a.Cost - b.Cost);
  
      // Update state with sorted data
      setData(sortedDataBudget);
  };
   
  const handlePrediction = () => {
    // Create an object containing the data to be sent in the request body
    const requestData = [
        installationType,
        panelType,
        capacity,
        maintenanceFrequency,
       predictBudget,
        region,
        typeOfInstallation,
        installerName,
        warranty,

    ];
    const finalJson = {
      "input": requestData
    }
    console.log(finalJson)
    // Make a POST request to the API endpoint
    fetch('http://localhost:5000/predict', {
      // mode: "no-cors",
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            
             // Specify the content type as JSON
        },
        body: JSON.stringify(finalJson), // Convert the data object to JSON string
    })
    .then(response => {
        if (!response.ok) {
          return response.json();
        }
        // console.log(response.json())

        // setPredictedAnnualSavings(respJsonn["Annual Savings"])
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        // Handle the response data
        console.log('Response:', data);
        setPredictedAnnualSavings(data["Annual Savings"])
        const roundedBreakEvenPoint = parseFloat(data["Break Even Point (years)"]).toFixed(2);
        setBreakEvenPoint(roundedBreakEvenPoint);
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
};

    return (
        <>
            <div className="w-1/2 mx-auto my-8">
                <div className="flex">
                    {/* First Select */}
                    <div className="flex flex-col w-1/2 mr-2">
                        <label className="text-white">State 1</label>
                        <Select className="h-full w-full" onChange={handleStateChange}>
                            <option value="0">Delhi</option>
                            <option value="1">Gujarat</option>
                            <option value="2">Karnataka</option>
                            <option value="3">Kerala</option>
                            <option value="4">Maharashtra</option>
                            <option value="5">Rajasthan</option>
                            <option value="6">Tamil Nadu</option>
                            <option value="7">Telangana</option>
                            <option value="8">Uttar Pradesh</option>
                            <option value="9">West Bengal</option>
                        </Select>
                    </div>
                    
                    {/* Second Select */}
                    <div className="flex flex-col w-1/2 ml-2 ">
                        <Label className='text-white mt-1' value='Budget'/>
                        <TextInput type='text' sizing="md" onChange={handleBudgetChange} />
                    </div>
                </div>
                
                <Button onClick={handleSortGrid} className='mt-4'>Sort Grid</Button>
                <div className="bg-white mt-4">

                <DataGrid
                className='text-white'
				rows={data}
				columns={columns}
				pageSize={10}
        
				// autoHeight
        getRowId={(row) => row.id}
				checkboxSelection
				disableSelectionOnClick
			/>

                </div>

            </div>
      <div className="w-3/4 mx-auto mb-32 bg-[#9cba9d]">

      <Label className='text-white text-2xl mb-8'>Predict for you:</Label>

     <div className="flex">

      <div className="flex flex-col mt-8 w-1/2">
        
      <Label className='text-white text-2xl mb-2 px-8'>Installation Type</Label>

      <Select onChange={handleInstallationType} className='px-8'>
      <option value="0">Commercial</option>
      <option value="1">Industrial</option>
      <option value="2">Residential</option>

      </Select>
      </div>

      <div className="flex flex-col mt-8 w-1/2">
        
      <Label className='text-white text-2xl mb-2 px-8'>Panel Type</Label>
      
      <Select onChange={handlePanelType} className='px-8'>
      <option value="0">Monocrystalline</option>
      <option value="1">Polycrystalline</option>
      <option value="2">Thin Film</option>

      </Select>
      </div>
     </div>
      <div className="flex">

      <div className="flex flex-col mt-8 w-1/2">
        
      <Label className='text-white text-2xl mb-2 px-8'>Capacity</Label>

      <TextInput onChange={handleCapacity} className='px-8'></TextInput>
      </div>
      <div className="flex flex-col mt-8 w-1/2">
        
      <Label className='text-white text-2xl mb-2 px-8'>Maintenance Frequency(months)</Label>

      <TextInput onChange={handleMaintainance} className='px-8'></TextInput>
      </div>
      
      </div>

<div className="flex">
  <div className="flex flex-col mt-8 w-1/2">
  <Label className='text-white text-2xl mb-2 px-8'> Region</Label>

<Select onChange={handleRegion} className='px-8'>
<option value="0">Delhi</option>
                            <option value="1">Gujarat</option>
                            <option value="2">Karnataka</option>
                            <option value="3">Kerala</option>
                            <option value="4">Maharashtra</option>
                            <option value="5">Rajasthan</option>
                            <option value="6">Tamil Nadu</option>
                            <option value="7">Telangana</option>
                            <option value="8">Uttar Pradesh</option>
                            <option value="9">West Bengal</option>
</Select>
  </div>
  <div className="flex flex-col mt-8 w-1/2">
  <Label className='text-white text-2xl mb-2 px-8'>Type Of Installation</Label>

<Select onChange={handleTypeOfInstallation} className='px-8'>
<option value="0">Ground mounted</option>
<option value="1">Roof mounted</option>

</Select>
  </div>
</div>

<div className="flex">
  <div className="flex flex-col mt-8 w-1/2">
  <Label className='text-white text-2xl mb-2 px-8'>Warranty (years)</Label>

<TextInput onChange={handleWarranty} className='px-8'></TextInput>
  </div>
  <div className="flex flex-col mt-8 w-1/2">
  <Label className='text-white text-2xl mb-2 px-8'>Installer Name</Label>

<Select onChange={handleInstallerName} className='px-8'>
<option value="0">GreenEnergy Co</option>
<option value="1">RaysPower Ltd</option>
<option value="2">SolarTech Pvt</option>
<option value="3">SunWave Ltd </option>


</Select>
  </div>
</div>
<div className="flex">
  <div className="flex flex-col mt-8 w-1/2">
  <Label className='text-white text-2xl mb-2 px-8'>Budget</Label>

<TextInput onChange={handlePredictBudget} className='px-8'></TextInput>
  </div>
  <div className="flex flex-col mt-8 w-1/2">


  </div>
</div>
<Button onClick={handlePrediction} className='mt-8 bg-green-700 w-32 mx-auto'>Predict</Button>

<Card className='mt-8 w-1/2 mx-auto text-3xl text-green-600' >Your predicted annual savings are: {predictedAnnualSavings} Rs</Card>
<Card className='mt-8 w-1/2 mx-auto text-3xl text-green-600' >Your break-even point is after: {breakEvenPoint} years </Card>

      </div>

        </>
    );
}

export default Solar;
