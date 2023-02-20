import { TestBed } from '@angular/core/testing';

import { SimilaruserService } from './similaruser.service';

describe('SimilaruserService', () => {
  let service: SimilaruserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SimilaruserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
