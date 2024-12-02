import React, { useEffect, useState } from "react";
import { Modal, ModalHeader, ModalBody, ModalFooter, Button, Form, Input } from "reactstrap";
import { getService, updateService } from "@/app/services/ServiceServices";

const ServiceEditModal = ({ isOpen, toggle, userId, serviceId,refresh }) => {
    const [CurrentService, setCurrentService] = useState({
        title: "",
        content: "",
        price: "",
        user_id: userId, // Default user_id
    });

    // Fetch the existing service data when editing
   useEffect(() => {
    const fetchServiceData = async () => {
        if (serviceId) {
            try {
                const fetchedService = await getService(serviceId);
                console.log("Fetched Service Data:", fetchedService);
                setCurrentService({
                    ...fetchedService,
                    user_id: userId,
                });
            } catch (error) {
                console.error("Error fetching service data:", error);
            }
        }
    };

    fetchServiceData();
}, [serviceId, userId]);


    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await updateService(serviceId, CurrentService).then(
                refresh()
            ); // Update the service with the new data
            toggle(); // Close the modal after successful update
        } catch (error) {
            console.error("Error updating service:", error);
        }
    };

    // Handle input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setCurrentService((prevState) => ({
            ...prevState,
            [name]: value, // Update the field based on the input's name
        }));
    };

    return (
        <Modal isOpen={isOpen} toggle={toggle}>
            <ModalHeader toggle={toggle}>Edit Service</ModalHeader>
            <ModalBody>
                <Form onSubmit={handleSubmit}>
                    <div>
                        <label className="block text-sm font-medium">Service Name</label>
                        <Input
                            type="text"
                            name="title"
                            value={CurrentService.title}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium">Description</label>
                        <Input
                            type="text"
                            name="content"
                            value={CurrentService.content}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium">Price</label>
                        <Input
                            type="number"
                            name="price"
                            value={CurrentService.price }
                            onChange={handleChange}
                            required
                        />
                    </div>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button color="success" onClick={handleSubmit}>
                    Save Changes
                </Button>
                <Button color="secondary" onClick={toggle}>
                    Cancel
                </Button>
            </ModalFooter>
        </Modal>
    );
};

export default ServiceEditModal;
