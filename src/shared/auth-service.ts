import { Injectable } from "@angular/core"
import { HttpClient } from "@angular/common/http"
import { AuthModel } from "./auth-model"

@Injectable({ providedIn:"root" })
export class AuthSevice{
    constructor( private http: HttpClient ){}

    addChore( name: string, weekday: string, description: string ) {

        const authData: AuthModel = { name: name, weekday: weekday, description: description }
        this.http.post('http:localhost:3000/chores/', authData).subscribe(res => {
            
        })
    }
}