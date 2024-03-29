
package ModuloSeguridad.Seguridad.Repositorios;

import org.springframework.data.mongodb.repository.Query;
import ModuloSeguridad.Seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
    @Query("{'url':?0,'metodo':?1}")
    Permiso getPermiso(String url, String metodo);
}