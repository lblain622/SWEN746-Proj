'use client';

import {useEffect, useRef, useState} from "react";
import {getUserServices,deleteService,updateService,createService} from "@/app/services/ServiceServices";
import {Card, CardBody, CardHeader, Form, FormGroup, Label, Input, Button, Spinner, Table} from 'reactstrap';
import ServiceCreateModal from "@/components/ServiceCreateModel";

export default function My_Services() {

    const [services,setServices] = useState(null);
    const [loading, setLoading] = useState(true);
    const [isEditing, setIsEditing] = useState(false);
    const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
    const[ user_Id,setUserId] = useState(null);
    const toggleCreate = () => setIsCreateModalOpen(!isCreateModalOpen);

    useEffect(() => {
        const fetchServices = async () => {
            try {
                const currentUser = JSON.parse(localStorage.getItem("currentUser"));

                if (currentUser && currentUser.id) {
                    setUserId(currentUser.id);
                    const data = await getUserServices(currentUser.id); // Fetch services data
                    setServices(data); // Set the services state
                }
            } catch (error) {
                console.error("Error fetching services:", error);
            } finally {
                setLoading(false); // Update loading state when fetching is complete
            }
        };

        fetchServices();
    }, []);

        const renderServices = (services) => {

            if (Array.isArray(services) && services.length > 0) {
                // Check if the array contains services
                return services.map((service) => (
                    <tr key={service.id}>
                        <td>{service.title || "No title available"}</td>
                        {/* Fallback text if title is missing */}
                        <td>{service.content || "No content available"}</td>
                        {/* Fallback text if content is missing */}
                        <td>{service.price || "No price available"}</td>
                        {/* Fallback text if price is missing */}
                        <td>
                            <Button color="warning" onClick={() => handleEdit(service)}>
                                Edit
                            </Button>{" "}
                            <Button color="danger" onClick={() => handleDelete(service.id)}>
                                Delete
                            </Button>
                        </td>
                    </tr>
                ));
            } else if (services) {
                // If it's a single service, render it
                console.log(services)
                return (
                    <tr key={services.id}>
                        <td>{services.title || "No title available"}</td>
                        <td>{services.content || "No content available"}</td>
                        <td>{services.price || "No price available"}</td>
                        <td>
                            <Button color="warning">Edit</Button>{" "}
                            <Button color="danger">Delete</Button>
                        </td>
                    </tr>
                );
            } else {
                // If no services exist, show "No services available"
                return (
                    <tr>
                        <td colSpan="4">No services available</td>
                    </tr>
                );
            }
        };


        return (
            <div>
                {loading ? (
                    <div>Loading...</div> // Show loading text
                ) : (
                    <Table>
                        <thead>
                        <tr>
                            <th>Title</th>
                            <th>Content</th>
                            <th>Price</th>
                            <th>Actions</th>
                        </tr>
                        </thead>
                        <tbody>{renderServices(services)}</tbody>
                    </Table>
                )}
                <Button color="primary" onClick={toggleCreate}>
                    <ServiceCreateModal
                        userId={user_Id}
                        toggle={toggleCreate}
                        isOpen={isCreateModalOpen}

                    />
                    Add Service
                </Button>
            </div>
        );

}
