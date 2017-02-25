export interface User {
    id: number;
    name: string;
    username: string;
    phone: string;
    email: string;
    website: string;
    address: Address
}
export interface Address {
    street: string;
    suite: string;
    city: string
}
