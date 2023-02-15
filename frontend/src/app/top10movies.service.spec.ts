import { TestBed } from '@angular/core/testing';

import { Top10moviesService } from './top10movies.service';

describe('Top10moviesService', () => {
  let service: Top10moviesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Top10moviesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
