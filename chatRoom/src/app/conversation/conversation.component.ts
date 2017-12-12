import { Component, OnInit, Input } from '@angular/core';
import { User } from '../user';
@Component({
  selector: 'app-conversation',
  templateUrl: './conversation.component.html',
  styleUrls: ['./conversation.component.css']
})
export class ConversationComponent implements OnInit {

  @Input() user: User;
  constructor() { }

  ngOnInit() {
  }

}
