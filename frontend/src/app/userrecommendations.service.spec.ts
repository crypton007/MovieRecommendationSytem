import { TestBed } from '@angular/core/testing';

import { UserrecommendationsService } from './userrecommendations.service';

describe('UserrecommendationsService', () => {
  let service: UserrecommendationsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserrecommendationsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
