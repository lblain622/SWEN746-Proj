'use client';

import React, { useState, useEffect } from 'react';
import { Row, Col, Card, CardBody, CardTitle, CardText, Button } from 'reactstrap';
import { Form, FormGroup } from 'reactstrap';
import { useRouter } from "next/navigation";

export default function Services() {
  const navigate = useRouter();

  const cardsPerPage = 3;
  const [currentPage, setCurrentPage] = useState(1);

  const [services, setServices] = useState([]);

  const startIndex = (currentPage - 1) * cardsPerPage;
  const endIndex = startIndex + cardsPerPage;

  const currentCards = services.slice(startIndex, endIndex);

  const [searchInput, setInput] = useState("");

  const handleNextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  const handlePreviousPage = () => {
    setCurrentPage(currentPage - 1);
  };

  useEffect(() => {
    const fetchServices = async () => {
      try {
          const response = await fetch(`http://localhost:5000/filter`);
          const data = await response.json();
          const transformed = data[0].map((service, index) => ({
            id: index + 1,
            title: service[0],
            content: service[1],
            price: service[2]
          }));
          setServices(transformed);
      } catch (error) {
        console.error("Error fetching services:", error);
      }
    };
    fetchServices();
  }, []);

  const handleChange = (e) => {
    e.preventDefault();
    setInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); 
      try {
        const response = await fetch(`http://localhost:5000/filter?service=${searchInput}`);
        const data = await response.json();
        const transformed = data[0].map((service, index) => ({
          id: index + 1,
          title: service[0],
          content: service[1],
          price: service[2]
        }));
        console.log(data);
        console.log(transformed);
        setServices(transformed); 
      } catch(error) {
        console.log(error);
      }
    setInput(""); 
  };

  const handleView = (id) => {
    navigate.push(`/detail/${id}`); 
  };

    return (
      <>
        <div>List of services</div>
      {/*Search Bar at Top*/}
      <Form onSubmit={handleSubmit}>
        <FormGroup>
        <input
          style={ {width:'80%', alignItems:'center', padding:'10px', fontSize:'16px'} }
          type="text"
          placeholder="Search here"
          onChange={handleChange}
          value={searchInput} 
        /> 
      </FormGroup>
    </Form>

      <div>
      {/* Grid Layout of Cards */} 
      <Row>
        {services.map((service) => (
          <Col sm="6" md="4" lg="3" key={service.id} className="mb-4">
            <Card>
              <CardBody>
                <CardTitle tag="h5">{service.title}</CardTitle>
                <CardText> 
                  {service.content}
              <br></br>
                  {service.price}
                </CardText>
                <Button style= {{backgroundColor:'grey'}}
                color="primary"
                onClick={() => handleView(service.id)}>
                View More
                </Button>
              </CardBody>
            </Card>
          </Col>
        ))}
      </Row>

      {/* Pagination Controls */}
      <div className="d-flex justify-content-around">
        <Button
          color="primary"
          disabled={currentPage === 1} // Disable "Previous" on first page
          onClick={handlePreviousPage}
        >
          Previous
        </Button>

        <Button
          color="primary"
          disabled={endIndex >= services.length} // Disable "Next" if we reached the last page
          onClick={handleNextPage}
        >
          Next
          </Button>
        </div>
      </div>
    </>

    );
  }

  const GETUSERURL = 'http://localhost:5000/services/user/';
const GETURL = 'http://localhost:5000/services/';
const POSTURL = 'http://localhost:5000/services/create';
const DELETEURL = 'http://localhost:5000/services/delete/';

export async function getUserServices(user_id) {
    try {
        const apiURL = GETUSERURL + user_id;
        const response = await fetch(apiURL, { method: 'GET' });

        if (!response.ok) {
             new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // If the data is a single service
        if (Array.isArray(data) && data.length === 6) {
            // Return the single service in the desired format
            return [{
                id: data[0],
                title: data[1],
                content: data[2],
                price: data[3],
                created_at: data[4],
                user_id: data[5],
            }];
        }

        // If the data is an array of services
        if (Array.isArray(data) && data.length > 0) {
            return data.map((servicedata) => ({
                id: servicedata[0],
                title: servicedata[1],
                content: servicedata[2],
                price: servicedata[3],
                created_at: servicedata[4],
                user_id: servicedata[5],
            }));
        }

        // If no services are returned, return an empty array
        return [];
    } catch (error) {
        console.error('Error fetching user services:', error);
        return [];  // Return an empty array in case of an error
    }
}


export async function getService(service_id) {
    try{
        const apiURL = GETURL+ service_id;
        const response = await fetch(apiURL,{method: 'GET'});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }
        const servicedata = await response.json();
        return {
            id: servicedata[0],
            title: servicedata[1],
            content: servicedata[2],
            price: servicedata[3],
            user_id: servicedata[5],
        }
    }catch(error){
        console.error(error);
    }
}

export async function updateService(service_id,data) {
    try{
        const apiURL = 'http://localhost:5000/services/update/'+service_id;
        const response = await fetch(apiURL,{
            method: 'PUT',
            headers: {'Content-Type': 'application/json',},
            body:JSON.stringify(data)});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
    console.error(error);
}
}
export async function createService(data){
    try{
        const response = await fetch(POSTURL,{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body:JSON.stringify(data)
        });

        console.log(JSON.stringify(data))
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
        console.error(error);
    }
}

export async function deleteService(service_id){
    try{
        const apiURL = DELETEURL+ service_id;
        const response = await fetch(apiURL,{method: 'DELETE'});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
        console.error(error);
    }
}
  