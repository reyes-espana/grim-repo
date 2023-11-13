import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddChoreComponent } from './add-chore.component';

describe('AddChoreComponent', () => {
  let component: AddChoreComponent;
  let fixture: ComponentFixture<AddChoreComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddChoreComponent]
    });
    fixture = TestBed.createComponent(AddChoreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
