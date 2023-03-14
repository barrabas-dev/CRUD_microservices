
package ModuloSeguridad.Seguridad.Repositorios;

import ModuloSeguridad.Seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {
}