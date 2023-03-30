import { Component, OnInit } from '@angular/core';
import { IplogService } from './services/iplog.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'IP address logger';
  iplog: any;

  constructor(private service:IplogService) {}

  ngOnInit() {
      this.service.getIplog()
        .subscribe(response => {
          this.iplog = response;
        });
  }
}
