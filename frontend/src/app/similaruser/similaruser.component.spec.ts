import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimilaruserComponent } from './similaruser.component';

describe('SimilaruserComponent', () => {
  let component: SimilaruserComponent;
  let fixture: ComponentFixture<SimilaruserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SimilaruserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimilaruserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
