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

  const handleSubmit = (e) => {
    e.preventDefault(); 
    setServices(services.filter(card => card.title === searchInput)); 
    setInput(""); 
  }

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
          style={ {width: '80%', alignItems:'center', padding: '10px', fontSize: '16px'} }
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
  