export class User {
    constructor(public id: number,
                public name: string,
                public username: string,
                public email: string,
                public phone: string,
                public website: string,
                public address: Address) {
    }
}
export class Address {
    constructor(public street: string,
                public suite: string,
                public city: string)
}
