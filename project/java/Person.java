package None;

import java.util.List;
import lombok.*;






/**
  Represents a Person
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends NamedThing {

  private String primaryEmail;
  private LocalDate birthDate;
  private Integer ageInYears;
  private String vitalStatus;

}