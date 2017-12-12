import { User } from './user';
import { USERS } from './mock-users';
import { Injectable } from '@angular/core';

@Injectable()
export class UsersService {

  constructor() { }

}

getUsers(): User[] {
  return USERS;
}