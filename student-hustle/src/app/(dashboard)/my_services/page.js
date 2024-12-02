'use client';
import { useCallback, useEffect, useState } from "react";
import { getUserServices, deleteService, updateService, createService } from "@/app/services/ServiceServices";
import {
    Card,
    CardBody,
    CardHeader,
    Form,
    FormGroup,
    Label,
    Input,
    Button,
    Spinner,
    Table,
    ModalBody,
    ModalFooter, Modal, ModalHeader
} from 'reactstrap';

import ServiceCreateModal from "@/components/ServiceCreateModel";
import ServiceUpdateModel from "@/components/ServiceUpdateModel";

export default function My_Services() {

    const [services, setServices] = useState(null);
    const [loading, setLoading] = useState(true);
    const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
    const [isUpdateModelOpen, setIsUpdateModalOpen] = useState(false);
    const [selectedServiceId, setSelectedServiceId] = useState(null);
    const [user_Id, setUserId] = useState(null);

    const toggleCreate = () => setIsCreateModalOpen(!isCreateModalOpen);
    const toggleDelete = (serviceId = null) => {
        setSelectedServiceId(serviceId);
        setIsDeleteModalOpen(!isDeleteModalOpen);
    };
    const toggleUpdate = (serviceId) => {
        setSelectedServiceId(serviceId);
        setIsUpdateModalOpen(!isUpdateModelOpen);
    };

    const refreshServices = useCallback(async () => {
        setLoading(true);  // Start loading spinner or indicator
        try {
            const updatedServices = await getUserServices(user_Id);

            if (updatedServices && Array.isArray(updatedServices)) {

                setServices(updatedServices);
            } else {
                console.error("No valid services data received");
                setServices([]);
            }
        } catch (error) {
            console.error("Error fetching updated services:", error);
            setServices([]);
        } finally {
            setLoading(false);
        }
    }, [user_Id]);

    useEffect(() => {
        const currentUser = JSON.parse(localStorage.getItem("currentUser"));
        setUserId(currentUser.id);
        if (user_Id && currentUser) {
            refreshServices();
        }
    }, [refreshServices, user_Id]);

    const confirmDelete = () => {
        if (selectedServiceId) {
            deleteService(selectedServiceId)
                .then(() => {
                    refreshServices();
                    toggleDelete();
                })
                .catch((err) => console.error("Error deleting service:", err));
        }
    };

    const renderServices = (services) => {
        if (Array.isArray(services) && services.length > 0) {
            return services.map((service) => (
                <tr key={service.id}>
                    <td>{service.title || "No title available"}</td>
                    <td>{service.content || "No content available"}</td>
                    <td>{service.price || "No price available"}</td>
                    <td>
                        <Button color="warning" onClick={() => toggleUpdate(service.id)}>
                            Edit
                        </Button>
                        {" "}
                        <Button color="danger" onClick={() => toggleDelete(service.id)}>
                            Delete
                        </Button>
                    </td>
                </tr>
            ));
        } else {
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
                <div>Loading...</div>
            ) : (
                <Table>
                    <thead>
                    <tr>
                        <th>Service Name</th>
                        <th>Description</th>
                        <th>Price</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>{renderServices(services)}</tbody>
                </Table>
            )}


            <ServiceUpdateModel
                isOpen={isUpdateModelOpen}
                userId={user_Id}
                serviceId={selectedServiceId}
                toggle={() => toggleUpdate(null)}
                refresh={refreshServices}
            />


            <Modal isOpen={isDeleteModalOpen} toggle={() => toggleDelete(null)}>
                <ModalHeader toggle={() => toggleDelete(null)}>Confirm Delete</ModalHeader>
                <ModalBody>
                    Are you sure you want to delete this service? This action cannot be undone.
                </ModalBody>
                <ModalFooter>
                    <Button color="danger" onClick={confirmDelete}>
                        Delete
                    </Button>
                    <Button color="secondary" onClick={() => toggleDelete(null)}>
                        Cancel
                    </Button>
                </ModalFooter>
            </Modal>


            <Button color="primary" onClick={toggleCreate}>
                Add Service
            </Button>
            <ServiceCreateModal
                userId={user_Id}
                toggle={toggleCreate}
                isOpen={isCreateModalOpen}
                refresh={refreshServices}  />
        </div>
    );
}
