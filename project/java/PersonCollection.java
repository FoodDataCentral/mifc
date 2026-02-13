package None;

import java.util.List;
import lombok.*;






/**
  A holder for Person objects
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonCollection  {

  private List<Person> entries;

}