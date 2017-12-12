import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here

import { AppComponent } from './app.component';
import { UsersComponent } from './users/users.component';
import { ConversationComponent } from './conversation/conversation.component';
import { UserService } from './user.service';


@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    ConversationComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
