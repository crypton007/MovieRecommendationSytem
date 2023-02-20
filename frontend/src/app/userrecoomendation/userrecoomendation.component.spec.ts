import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserrecoomendationComponent } from './userrecoomendation.component';

describe('UserrecoomendationComponent', () => {
  let component: UserrecoomendationComponent;
  let fixture: ComponentFixture<UserrecoomendationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UserrecoomendationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UserrecoomendationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
