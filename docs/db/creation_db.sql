--
-- Name: document_type
--

CREATE TABLE document_type (
    id SERIAL PRIMARY KEY,
    type character varying(100) NOT NULL,
    type_abreviation character varying(2) NOT NULL
);


--
-- Name: gender
--

CREATE TABLE gender (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: users
--

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    document_type_id INTEGER NOT NULL,
    document_number character varying(15) NOT NULL,
    name character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    username character varying(100) NOT NULL,
    password text NOT NULL,
    is_active boolean NOT NULL,
    gender_id INTEGER NOT NULL,

    FOREIGN KEY (document_type_id) REFERENCES document_type(id),
    FOREIGN KEY (gender_id) REFERENCES gender(id),
    CONSTRAINT unique_doc_num UNIQUE (document_number)
);


--
-- Name: nutritionist
--

CREATE TABLE nutritionist (
    id INTEGER PRIMARY KEY,

    FOREIGN KEY (id) REFERENCES users(id)
);


--
-- Name: patient
--
-- Posible mejora: Agregar una tabla extra para llevar un histórico de los pesos de los pacientes (saber cuánto ha pesado en cada fecha para saber cómo ha avanzado)

CREATE TABLE patient (
    id INTEGER PRIMARY KEY,
    weight numeric(10,2) NOT NULL,
    height numeric(10,2) NOT NULL,
    year_birth integer NOT NULL,
    nutritionist_id INTEGER NOT NULL,

    FOREIGN KEY (id) REFERENCES users(id),
    FOREIGN KEY (nutritionist_id) REFERENCES nutritionist(id)
);


--
-- Name: special_condition
--

CREATE TABLE special_condition (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: patient_special_condition
--

CREATE TABLE patient_special_condition (
    patient_id INTEGER NOT NULL,
    special_condition_id INTEGER NOT NULL,

    PRIMARY KEY (patient_id, special_condition_id),
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (special_condition_id) REFERENCES special_condition(id)
);


--
-- Name: macronutrient_group
--

CREATE TABLE macronutrient_group (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: micronutrient_group
--

CREATE TABLE micronutrient_group (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: food_group
--

CREATE TABLE food_group (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: food_moment
--

CREATE TABLE food_moment (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);


--
-- Name: food_exchange
--

CREATE TABLE food_exchange (
    id SERIAL PRIMARY KEY,
    food_name text NOT NULL,
    weight numeric(10,2) NOT NULL,
    home_measurement character varying(100) NOT NULL,
    food_group_id INTEGER NOT NULL,
    macronutrient_group_id INTEGER NOT NULL,
    kcal integer DEFAULT 0 NOT NULL,

    FOREIGN KEY (food_group_id) REFERENCES food_group(id),
    FOREIGN KEY (macronutrient_group_id) REFERENCES macronutrient_group(id)
);

--
-- Name: food_exchange_macronutrient_contribution
--

CREATE TABLE food_exchange_macronutrient_contribution (
    food_exchange_id INTEGER NOT NULL,
    macronutrient_group_id INTEGER NOT NULL,
    contribution_quantity numeric(10,2) NOT NULL,
    measurement_unit character varying(5) NOT NULL,
    
    PRIMARY KEY (food_exchange_id, macronutrient_group_id),
    FOREIGN KEY (food_exchange_id) REFERENCES food_exchange(id),
    FOREIGN KEY (macronutrient_group_id) REFERENCES macronutrient_group(id)
);


--
-- Name: food_exchange_micronutrient_contribution
--

CREATE TABLE food_exchange_micronutrient_contribution (
    food_exchange_id INTEGER NOT NULL,
    micronutrient_group_id INTEGER NOT NULL,
    contribution_quantity numeric(10,2) NOT NULL,
    measurement_unit character varying(5) NOT NULL,
    
    PRIMARY KEY (food_exchange_id, micronutrient_group_id),
    FOREIGN KEY (food_exchange_id) REFERENCES food_exchange(id),
    FOREIGN KEY (micronutrient_group_id) REFERENCES micronutrient_group(id)
);

--
-- Name: eating_plan
--

CREATE TABLE eating_plan (
    id SERIAL PRIMARY KEY,
    description text NOT NULL,
    total_kcal integer NOT NULL,
    patient_id INTEGER NOT NULL,
    author_nutritionist_id INTEGER NOT NULL,

    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (author_nutritionist_id) REFERENCES nutritionist(id)
);


--
-- Name: food_moment_food_exchange
--

CREATE TABLE food_moment_food_exchange (
    eating_plan_id INTEGER NOT NULL,
    food_exchange_id INTEGER NOT NULL,
    food_moment_id INTEGER NOT NULL,
    food_exchange_quantity integer NOT NULL,

    PRIMARY KEY (eating_plan_id, food_exchange_id, food_moment_id),
    FOREIGN KEY (eating_plan_id) REFERENCES eating_plan(id),
    FOREIGN KEY (food_exchange_id) REFERENCES food_exchange(id),
    FOREIGN KEY (food_moment_id) REFERENCES food_moment(id)
);


--
-- Name: recipe
--

CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name character varying(100) NOT NULL,
    description text
);


--
-- Name: recipe_eating_plan
--

CREATE TABLE recipe_eating_plan (
    recipe_id INTEGER NOT NULL,
    food_moment_id INTEGER NOT NULL,
    eating_plan_id INTEGER NOT NULL,

    PRIMARY KEY (recipe_id, food_moment_id, eating_plan_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (food_moment_id) REFERENCES food_moment(id),
    FOREIGN KEY (eating_plan_id) REFERENCES eating_plan(id)
);


--
-- Name: recipe_ingredient
--

CREATE TABLE recipe_ingredient (
    recipe_id INTEGER NOT NULL,
    food_exchange_id INTEGER NOT NULL,
    food_exchange_quantity integer NOT NULL,

    PRIMARY KEY (recipe_id, food_exchange_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (food_exchange_id) REFERENCES food_exchange(id)
);