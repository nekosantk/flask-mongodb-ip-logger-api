import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class IplogService {
  private url = 'http://localhost:8000/api/myip';

  constructor(private httpClient: HttpClient) { }

  getIplog(){
    return this.httpClient.get(this.url, {responseType: 'text'});
  }
}
