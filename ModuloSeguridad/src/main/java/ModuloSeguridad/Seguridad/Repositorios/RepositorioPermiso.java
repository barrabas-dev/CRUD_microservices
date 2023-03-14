
package ModuloSeguridad.Seguridad.Repositorios;

import ModuloSeguridad.Seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
}