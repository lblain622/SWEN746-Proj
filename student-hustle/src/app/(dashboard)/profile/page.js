'use client';

import {useEffect, useRef, useState} from "react";
import {getProfile,updateProfile} from "@/app/services/ProfileService";
import { Card, CardBody, CardHeader, Form, FormGroup, Label, Input, Button,Spinner } from 'reactstrap';



export default function Profile() {
    const [formData, setFormData] = useState(null);
    const [profile_id, setProfileId] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const fetchProfile = async () => {
            const currentUser = JSON.parse(localStorage.getItem("currentUser"));
            if (currentUser && currentUser.id) {
                try {
                    setLoading(true);  // Start loading
                    const data = await getProfile(currentUser.id);
                    setProfileId(data.id);
                    setFormData(data);
                    setLoading(false);  // Stop loading after data is fetched
                } catch (error) {
                    console.error('Error fetching profile data:', error);
                    setLoading(false);  // Stop loading if there's an error
                }
            } else {
                setLoading(false);  // Stop loading if no user is found
            }
        };

        fetchProfile();
    }, []);
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleEditClick = () => {
        setIsEditing(true);
    };

    const handleSaveClick = () => {
        setIsEditing(false);
        console.log(formData.id);
        updateProfile(profile_id, formData);
        console.log("Updated Profile Data:", formData);

    };

    if (loading) {
        return <Spinner>Loading...</Spinner>;
    }
    return (
    <Card className="max-w-auto mx-auto">
        <CardHeader className="bg-white">
            <h2 className="text-xl font-bold">Profile Information</h2>
        </CardHeader>
        <CardBody>
            {isEditing ? (
                <Form>
                    <FormGroup>
                        <Label for="first_name">First Name:</Label>
                        <Input
                            type="text"
                            name="first_name"
                            id="first_name"
                            value={formData.first_name}
                            onChange={handleInputChange}
                        />
                    </FormGroup>

                    <FormGroup>
                        <Label for="last_name">Last Name:</Label>
                        <Input
                            type="text"
                            name="last_name"
                            id="last_name"
                            value={formData.last_name}
                            onChange={handleInputChange}
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for="age">Age:</Label>
                        <Input
                            type="number"
                            name="age"
                            id="age"
                            value={formData.age}
                            onChange={handleInputChange}
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label>Sex:</Label>
                        <div className="d-flex gap-4">
                            <Label check>
                                <Input
                                    type="radio"
                                    name="sex"
                                    value="M"
                                    checked={formData.sex === "M"}
                                    onChange={handleInputChange}
                                /> Male
                            </Label>
                            <Label check>
                                <Input
                                    type="radio"
                                    name="sex"
                                    value="F"
                                    checked={formData.sex === "F"}
                                    onChange={handleInputChange}
                                /> Female
                            </Label>
                        </div>
                    </FormGroup>

                    <Button color="success" onClick={handleSaveClick}>Save</Button>
                </Form>
            ) : (
                <div>
                    <p><strong>First Name:</strong> {formData.first_name}</p>
                    <p><strong>Last Name:</strong> {formData.last_name}</p>
                    <p><strong>Age:</strong> {formData.age}</p>
                    <p><strong>Sex:</strong> {formData.sex === "M" ? "Male" : "Female"}</p>
                    <Button color="primary" onClick={handleEditClick}>Edit</Button>
                </div>
            )}
        </CardBody>
    </Card>

    );
}
