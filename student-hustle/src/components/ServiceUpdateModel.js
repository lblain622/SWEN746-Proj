import React, { useState } from 'react';
import { Modal, ModalHeader, ModalBody, ModalFooter, Button, Form, Input } from 'reactstrap';
import { createService } from "@/app/services/ServiceServices"; // Assuming path is correct

const ServiceModal = ({ isOpen, toggle, userId }) => {
    const [newService, setNewService] = useState({ title: "", content: "", price: 0, user_id: userId });

    const handleSubmit = (e) => {
        e.preventDefault();
        createService(userId, newService); // Assuming createService is working as intended
        setNewService({ title: "", content: "", price: 0, user_id: userId }); // Reset form
        toggle(); // Close modal
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNewService((prevState) => ({
            ...prevState,
            [name]: value, // Update the correct field
        }));
    };

    return (
        <Modal isOpen={isOpen} toggle={toggle}>
            <ModalHeader toggle={toggle}>Add New Service</ModalHeader>
            <ModalBody>
                <Form onSubmit={handleSubmit}>
                    <div>
                        <label className="block text-sm font-medium">Service Name</label>
                        <Input
                            type="text"
                            name="title" // Correct name for title
                            value={newService.title}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium">Description</label>
                        <Input
                            type="text"
                            name="content" // Correct name for content
                            value={newService.content}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium">Price</label>
                        <Input
                            type="number"
                            name="price" // Correct name for price
                            value={newService.price}
                            onChange={handleChange}
                            required
                        />
                    </div>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button color="success" onClick={handleSubmit}>
                    Add Service
                </Button>
                <Button color="secondary" onClick={toggle}>
                    Cancel
                </Button>
            </ModalFooter>
        </Modal>
    );
};

export default ServiceModal;

