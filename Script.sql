-- ################
-- #    SCHEMA    #
-- ################

CREATE SCHEMA zone;

-- ################
-- #  SEQUENCES   #
-- ################

CREATE SEQUENCE zone.usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;


CREATE SEQUENCE zone.cartao_credito_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.ticket_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.marca_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.veiculo_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.compra_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.usuario_veiculo_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

CREATE SEQUENCE zone.estacionamento_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

-- ################
-- #    TABLES    #
-- ################

CREATE TABLE zone.tb_usuario_usu (
	id_usuario_usu integer NOT NULL DEFAULT nextval('zone.usuario_seq'::regclass),
	txt_nome_usu varchar(200) NOT NULL,
	txt_email_usu varchar(200) NOT NULL,
  txt_cpf_usu varchar(11) NOT NULL,
	CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario_usu)
);

CREATE TABLE zone.tb_marca_mar (
	id_marca_mar integer NOT NULL DEFAULT nextval('zone.marca_seq'::regclass),
	txt_marca_mar varchar(200) NOT NULL,
  txt_abreviacao_marca_mar varchar(10),
  img_marca_mar bytea NULL,
	dat_inicio_mar timestamp without time zone NOT null default now(),
	dat_fim_mar timestamp without time zone default null,
	CONSTRAINT marca_pkey PRIMARY KEY (id_marca_mar)
);

CREATE TABLE zone.tb_ticket_tic (
	id_ticket_tic integer NOT NULL DEFAULT nextval('zone.ticket_seq'::regclass),
	txt_descricao_tic varchar(100) NOT NULL,
  num_valor_tic real not null,
  num_horas_tic smallint not null,
	dat_inicio_tic timestamp without time zone NOT null default now(),
	dat_fim_tic timestamp without time zone default null,
	CONSTRAINT ticket_pkey PRIMARY KEY (id_ticket_tic)
);

CREATE TABLE zone.tb_veiculo_vei (
	id_veiculo_vei integer NOT NULL DEFAULT nextval('zone.veiculo_seq'::regclass),
  id_marca_vei integer NOT NULL,
  txt_veiculo_vei varchar(200) NOT NULL,
  img_veiculo_vei bytea NULL,
	dat_inicio_vei timestamp without time zone NOT null default now(),
	dat_fim_vei timestamp without time zone default null,
	CONSTRAINT veiculo_pkey PRIMARY KEY (id_veiculo_vei)
);
ALTER TABLE zone.tb_veiculo_vei ADD CONSTRAINT marca_fkey FOREIGN KEY (id_marca_vei) REFERENCES zone.tb_marca_mar (id_marca_mar);

CREATE TABLE zone.tb_usuario_veiculo_uve (
	id_usuario_veiculo_uve integer NOT NULL DEFAULT nextval('zone.usuario_veiculo_seq'::regclass),
  id_usuario_uve integer NOT NULL,
  id_veiculo_uve integer NOT NULL,
  txt_placa_uve varchar(7) NOT NULL,
	dat_inicio_uve timestamp without time zone NOT null default now(),
	dat_fim_uve timestamp without time zone default null,
	CONSTRAINT usuario_veiculo_pkey PRIMARY KEY (id_usuario_veiculo_uve)
);
ALTER TABLE zone.tb_usuario_veiculo_uve ADD CONSTRAINT usuario_fkey FOREIGN KEY (id_usuario_uve) REFERENCES zone.tb_usuario_usu (id_usuario_usu);
ALTER TABLE zone.tb_usuario_veiculo_uve ADD CONSTRAINT veiculo_fkey FOREIGN KEY (id_veiculo_uve) REFERENCES zone.tb_veiculo_vei (id_veiculo_vei);

CREATE TABLE zone.tb_cartao_credito_ccr (
	id_cartao_credito_ccr integer NOT NULL DEFAULT nextval('zone.cartao_credito_seq'::regclass),
  id_usuario_ccr integer NOT NULL,
	txt_numero_ccr varchar(16) NOT NULL,
  txt_nome_ccr varchar(100) NOT NULL,
  txt_validade_ccr varchar(7) NOT NULL,
  txt_cvc_ccr varchar(3) NOT NULL,
  dat_inicio_ccr timestamp without time zone NOT null default now(),
	dat_fim_ccr timestamp without time zone default null,
	CONSTRAINT cartao_Credito_pkey PRIMARY KEY (id_cartao_credito_ccr)
);
ALTER TABLE zone.tb_cartao_credito_ccr ADD CONSTRAINT usuario_fkey FOREIGN KEY (id_usuario_ccr) REFERENCES zone.tb_usuario_usu (id_usuario_usu);

CREATE TABLE zone.tb_compra_com (
	id_compra_com integer NOT NULL DEFAULT nextval('zone.compra_seq'::regclass),
  id_cartao_credito_com integer NOT NULL,
  id_ticket_com integer NOT NULL,
  qtd_cartao_com smallint NOT NULL,
	dat_inicio_sdo timestamp without time zone NOT null default now(),
	CONSTRAINT compra_pkey PRIMARY KEY (id_compra_com)
);
ALTER TABLE zone.tb_compra_com ADD CONSTRAINT cartao_credito_fkey FOREIGN KEY (id_cartao_credito_com) REFERENCES zone.tb_cartao_credito_ccr (id_cartao_credito_ccr);
ALTER TABLE zone.tb_compra_com ADD CONSTRAINT ticket_fkey FOREIGN KEY (id_ticket_com) REFERENCES zone.tb_ticket_tic (id_ticket_tic);

CREATE TABLE zone.tb_estacionamento_est (
	id_estacionamento_est integer NOT NULL DEFAULT nextval('zone.estacionamento_seq'::regclass),
  id_usuario_veiculo_est integer NOT NULL,
  id_compra_est integer NOT NULL,
	dat_inicio_est timestamp without time zone NOT null default now(),
	CONSTRAINT estacionamento_pkey PRIMARY KEY (id_estacionamento_est)
);
ALTER TABLE zone.tb_estacionamento_est ADD CONSTRAINT usuario_veiculo_fkey FOREIGN KEY (id_usuario_veiculo_est) REFERENCES zone.tb_usuario_veiculo_uve (id_usuario_veiculo_uve);
ALTER TABLE zone.tb_estacionamento_est ADD CONSTRAINT compra_fkey FOREIGN KEY (id_compra_est) REFERENCES zone.tb_compra_com (id_compra_com);


-- ####################################
-- #        INSERTS PARA TESTES       #
-- ####################################

INSERT INTO zone.tb_usuario_usu (txt_nome_usu, txt_email_usu, txt_cpf_usu) VALUES('Usuário', 'user@urbanzone.com.br', '1111111111');

INSERT INTO "zone".tb_marca_mar (txt_marca_mar, txt_abreviacao_marca_mar, img_marca_mar, dat_inicio_mar, dat_fim_mar) VALUES('TOYOTA', 'TOYOTA', NULL, now(), null);

INSERT INTO "zone".tb_veiculo_vei (id_marca_vei, txt_veiculo_vei, img_veiculo_vei, dat_inicio_vei, dat_fim_vei) VALUES(1, 'COROLLA', NULL, now(), NULL);
INSERT INTO "zone".tb_veiculo_vei (id_marca_vei, txt_veiculo_vei, img_veiculo_vei, dat_inicio_vei, dat_fim_vei) VALUES(1, 'COROLLA CROSS', NULL, now(), NULL);
INSERT INTO "zone".tb_veiculo_vei (id_marca_vei, txt_veiculo_vei, img_veiculo_vei, dat_inicio_vei, dat_fim_vei) VALUES(1, 'HILUX', NULL, now(), NULL);

INSERT INTO "zone".tb_ticket_tic (txt_descricao_tic, num_valor_tic, num_horas_tic, dat_inicio_tic, dat_fim_tic) VALUES('ZONE 1h', 1.00, 1, now(), NULL);
INSERT INTO "zone".tb_ticket_tic (txt_descricao_tic, num_valor_tic, num_horas_tic, dat_inicio_tic, dat_fim_tic) VALUES('ZONE 2h', 1.00, 1, now(), NULL);
