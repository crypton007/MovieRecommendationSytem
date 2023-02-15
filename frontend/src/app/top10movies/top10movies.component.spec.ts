import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Top10moviesComponent } from './top10movies.component';

describe('Top10moviesComponent', () => {
  let component: Top10moviesComponent;
  let fixture: ComponentFixture<Top10moviesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Top10moviesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Top10moviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
